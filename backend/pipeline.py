import ingest
import llm_processor

if __name__ == "__main__":
    ingest.fetch()
    llm_processor.run_llm()
    print("Pipeline complete.")