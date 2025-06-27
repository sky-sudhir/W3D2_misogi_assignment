def get_model_metadata(model_name):
    metadata = {
        "gemini": {
            "type": "Instruct",
            "source": "Google",
            "instruction_following": True,
            "fine_tuning": "Proprietary instruction tuning + alignment",
            "context_window": "32K+ tokens",
        },
        "qwen2.5:3b": {
            "type": "Fine-tuned Instruct",
            "source": "Alibaba",
            "instruction_following": True,
            "fine_tuning": "Supervised fine-tuning + chat alignment",
            "context_window": "32K tokens",
        }
    }
    return metadata.get(model_name.lower(), {})
