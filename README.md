# AI Interview Mentor - LangChain Project

## Overview

AI Interview Mentor is a Generative AI project built using LangChain and Google's Gemini model.

This application acts as a professional interview coach that:

* Maintains conversation memory
* Understands the user's role
* Generates interview questions
* Provides interview instructions
* Shares expert advice
* Returns responses in a structured format using Pydantic Output Parser

---

## Features

### 1. Conversational Memory

The chatbot remembers previous interactions using:

* RunnableWithMessageHistory
* InMemoryChatMessageHistory

This allows natural multi-turn interview preparation.

---

### 2. Structured Outputs

Responses are generated in a predefined schema:

```python
class InterviewModel(BaseModel):
    interview: str
    instructions: str
    expert: str
```

---

### 3. Gemini Integration

Uses:

```python
ChatGoogleGenerativeAI
```

to access Google's Gemini model.

---

### 4. Interview Preparation

The assistant can:

* Ask role-specific interview questions
* Give confidence-building instructions
* Share professional interview advice

---

## Tech Stack

* Python
* LangChain
* Gemini API
* Pydantic
* dotenv

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Interview-Mentor-LangChain.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run:

```bash
python main.py
```

---

## Example

User:

```text
I am preparing for a Python Developer role
```

Output:

Interview Questions:

* What is the difference between a list and tuple?
* Explain OOP principles.

Instructions:

* Maintain eye contact.
* Listen carefully before answering.
* Use the STAR method.

Expert Advice:

* Practice mock interviews.
* Focus on communication.
* Explain your thought process.

---

## LangChain Concepts Used

* Chat Models
* Prompt Engineering
* Output Parsers
* Pydantic Schema
* Chat Memory
* Runnable Chains
* Message History

---

## Future Improvements

* Streamlit UI
* Resume Analyzer
* Voice Interview Support
* Interview Scoring System
* RAG-based Company Interview Preparation

---

## Author

Sandeep Pilli

AI & ML Student | Generative AI Learner | LangChain Enthusiast
