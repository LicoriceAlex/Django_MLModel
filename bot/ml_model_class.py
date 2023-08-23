from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


class RobertaBaseSquad2:
    def __init__(self):
        model_name = "deepset/roberta-base-squad2"
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.pipeline = pipeline(
            'question-answering',
            model=model_name,
            tokenizer=model_name
        )

    def get_answer(self, question: str, context: str) -> str:
        QA_input = {
            'question': question,
            'context': context
        }
        answer = self.pipeline(QA_input).get('answer')
        return answer
