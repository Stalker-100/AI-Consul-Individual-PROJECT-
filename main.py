import os
from dotenv import load_dotenv
from groq import Groq

# загрузка API ключа из .env
load_dotenv()

# инициализация Groq
client = Groq()

# история
history = [
    {
        "role": "system",
        "content": "Ты — консультант по курсам колледжа Академия ТОП. Отвечай как профессиональный менеджер, коротко и по делу, максимум 2-3 предложения."
    }
]


def ask_groq(question: str) -> str:
    # добавить запрос в историю
    history.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=history,  # передать накопленную историю
        max_tokens=600
    )

    # ответ
    answer = response.choices[0].message.content

    # сохраняем ответ ассистента и передаем снова в историю
    history.append({"role": "assistant", "content": answer})

    return answer


print("Ассистент готов! Задай вопрос ('выход' - завершить)")

while True:
    user_input = input('> ')
    if user_input.lower() in ("выход", "exit", "quit"):
        break
    print(ask_groq(user_input))
