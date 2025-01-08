import yaml


def load_prompt(prompt_name: str, **kwargs) -> str:
    """
    Load a specific prompt from the YAML configuration and fill placeholders.

    Args:
        prompt_name (str): The key for the desired prompt.
        **kwargs: Placeholder values to format the prompt.

    Returns:
        str: Formatted prompt string.
    """
    try:
        with open("../configs/prompts.yaml", "r") as file:
            prompts = yaml.safe_load(file)

        if prompt_name not in prompts:
            raise ValueError(f"[ERROR] Prompt '{prompt_name}' not found in YAML file.")

        prompt_template = prompts[prompt_name]["prompt"]

        return prompt_template.replace("{{text}}", kwargs.get("text", "")).replace(
            "{{max_facts}}", str(kwargs.get("max_facts", 5))
        )

    except KeyError as e:
        print(f"[ERROR] Missing key in placeholder replacement: {e}")
        return ""
    except Exception as e:
        print(f"[ERROR] Failed to load prompt: {e}")
        return ""
