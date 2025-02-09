from transformers import T5Tokenizer, T5ForConditionalGeneration

def process_text(input_text, task="summarize"):
    """Process text (summarize or other tasks) using a pre-trained T5 model."""
    # Load the pre-trained model and tokenizer for T5
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    tokenizer = T5Tokenizer.from_pretrained("t5-small")

    # Prepare the input for the model
    input_ids = tokenizer.encode(f"{task}: {input_text}", return_tensors="pt")

    # Generate the output text
    output_ids = model.generate(input_ids, max_length=200, num_beams=4, early_stopping=True)

    # Decode the output text and return
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output_text
