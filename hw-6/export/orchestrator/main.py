import asyncio
import json
import os

from typing import AsyncGenerator
from util import logger

import prompt
import openai
from retrieval import Retriever
from retrieval.search import GoogleAPI
from retrieval.scraper import ScraperLocal, ScraperRemote
from retrieval.embeddings import OpenAIEmbeddings
from retrieval.splitter import LangChainSplitter


# NOTE: We're overriding the API base URL and key to use a mock server for local testing
# This allows us to test the application without requiring actual OpenAI API credentials
openai.api_base = "http://127.0.0.1:8000/v1"
openai.api_key = "dummy-key"  # No se valida en un servidor local

def stream_chat(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}],
        stream=False,  # Forzar modo no streaming
    )
    if isinstance(response, dict) and "choices" in response:
        content = response["choices"][0]["message"]["content"]
        if content is not None:
            yield content


async def event_generator(query) -> AsyncGenerator[dict, None]:
    embeddings = OpenAIEmbeddings()
    google = GoogleAPI()
    scraper = ScraperLocal()
    splitter = LangChainSplitter(chunk_size=400, chunk_overlap=50, length_function=len)

    retriever = Retriever(
        searcher=google,
        scraper=scraper,
        embeddings=embeddings,
        splitter=splitter,
    )
    async for event in retriever.get_context(query=query, cache_treshold=0.85, k=10):
        yield event
        if event["event"] == "context":
            final_prompt = prompt.rag.format(context=event["data"], question=query)
            yield {"event": "prompt", "data": final_prompt}
            for text in stream_chat(prompt=final_prompt):
                yield {"event": "token", "data": text}


async def main(query: str):
    async for event in event_generator(query):
        if event["event"] == "search":
            for link in json.loads(event["data"])["items"]:
                print(f"Link: {link['link']}")
            print(" ")
        if event["event"] == "token":
            print(event["data"], end="", flush=True)


if __name__ == "__main__":
    while True:
        print("")
        query = input(">Enter your question: ")
        print("")
        asyncio.run(main(query))
        print("")
