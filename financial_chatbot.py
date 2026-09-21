import pandas as pd

# Financial data from Task 1
data = [
    ["Microsoft", 2023, 211915, 72361, 411976, 205753, 87582],
    ["Microsoft", 2024, 245122, 88136, 512163, 243686, 118548],
    ["Microsoft", 2025, 281724, 101832, 619003, 275524, 136162],

    ["Tesla", 2023, 96773, 14974, 106618, 43009, 13256],
    ["Tesla", 2024, 97690, 7153, 122070, 48390, 14923],
    ["Tesla", 2025, 94827, 3855, 137806, 54941, 14747],

    ["Apple", 2023, 383285, 96995, 352583, 290437, 110543],
    ["Apple", 2024, 391035, 93736, 364980, 308030, 118254],
    ["Apple", 2025, 416161, 112010, 359241, 285508, 111482]
]

columns = [
    "Company",
    "Fiscal Year",
    "Total Revenue",
    "Net Income",
    "Total Assets",
    "Total Liabilities",
    "Operating Cash Flow"
]

df = pd.DataFrame(data, columns=columns)


def financial_chatbot(user_query):

    question = user_query.lower().strip()

    # Greeting
    if any(word in question.split() for word in ["hello", "hi", "hey"]):
        return (
            "Hello! I am the GFC Financial Chatbot. "
            "I can answer questions about Microsoft, Tesla, and Apple "
            "financial performance from 2023 to 2025."
        )

    # Help
    if "help" in question or "what can you do" in question:
        return (
            "I can provide information about revenue, net income, "
            "operating cash flow, total assets, and total liabilities "
            "for Microsoft, Tesla, and Apple from 2023 to 2025."
        )

    # Identify company
    company = None

    if "microsoft" in question:
        company = "Microsoft"
    elif "tesla" in question:
        company = "Tesla"
    elif "apple" in question:
        company = "Apple"

    if company is None:
        return (
            "Sorry, I could not identify a supported company. "
            "Please ask about Microsoft, Tesla, or Apple."
        )

    # Revenue change
    if "revenue" in question and "change" in question:

        start = df[
            (df["Company"] == company) &
            (df["Fiscal Year"] == 2023)
        ]["Total Revenue"].iloc[0]

        end = df[
            (df["Company"] == company) &
            (df["Fiscal Year"] == 2025)
        ]["Total Revenue"].iloc[0]

        change = ((end - start) / start) * 100

        direction = "increased" if change >= 0 else "decreased"

        return (
            f"{company}'s revenue {direction} by {abs(change):.2f}% "
            f"from 2023 to 2025, changing from "
            f"${start:,.0f} million to ${end:,.0f} million."
        )

    # Identify year
    year = None

    for y in [2025, 2024, 2023]:
        if str(y) in question:
            year = y
            break

    # Identify financial metric
    if "revenue" in question:
        metric = "Total Revenue"
        label = "revenue"

    elif "net income" in question or "profit" in question:
        metric = "Net Income"
        label = "net income"

    elif "cash flow" in question or "operating cash" in question:
        metric = "Operating Cash Flow"
        label = "operating cash flow"

    elif "assets" in question:
        metric = "Total Assets"
        label = "total assets"

    elif "liabilities" in question:
        metric = "Total Liabilities"
        label = "total liabilities"

    else:
        return (
            "Sorry, I could not understand that financial query. "
            "Try asking about revenue, net income, operating cash flow, "
            "assets, or liabilities."
        )

    if year is None:
        return "Please specify a fiscal year: 2023, 2024, or 2025."

    row = df[
        (df["Company"] == company) &
        (df["Fiscal Year"] == year)
    ]

    if row.empty:
        return "Sorry, no matching financial data was found."

    value = row.iloc[0][metric]

    return (
        f"{company}'s {label} in {year} was "
        f"${value:,.0f} million."
    )


# Test the chatbot
if __name__ == "__main__":

    test_questions = [
        "What is Microsoft's revenue in 2025?",
        "What is Tesla's net income in 2024?",
        "What is Apple's revenue in 2025?",
        "What was Microsoft's operating cash flow in 2025?",
        "What were Apple's total assets in 2025?",
        "What were Tesla's total liabilities in 2025?",
        "How did Microsoft's revenue change from 2023 to 2025?",
        "Hello",
        "What can you do?",
        "Tell me about Google's revenue"
    ]

    print("GFC Financial Chatbot - Test Results")
    print("=" * 70)

    for question in test_questions:
        print("User:", question)
        print("Bot:", financial_chatbot(question))
        print("-" * 70)

    print("\nInteractive mode: type 'exit' to stop.")

    while True:

        user_question = input("You: ")

        if user_question.lower().strip() == "exit":
            print("Bot: Thank you for using the GFC Financial Chatbot.")
            break

        print("Bot:", financial_chatbot(user_question))