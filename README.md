# BCG GenAI Job Simulation - Task 2
## Financial Chatbot Prototype

### Objective

This project demonstrates a simple rule-based financial chatbot for Global Finance Corp. (GFC).

The chatbot uses financial data for Microsoft, Tesla, and Apple for fiscal years 2023–2025.

### Predefined Queries

The chatbot can answer questions about:

- Total Revenue
- Net Income
- Operating Cash Flow
- Total Assets
- Total Liabilities
- Revenue change from 2023 to 2025
- Basic greetings and help requests

### How It Works

The chatbot is developed using Python, pandas, and rule-based if/elif logic.

1. Financial data is stored in a pandas DataFrame.
2. The user's question is converted to lowercase.
3. The chatbot identifies the company.
4. It identifies the financial year.
5. It identifies the requested financial metric.
6. It retrieves the corresponding value.
7. It generates a simple natural-language response.

### Error Handling

If the chatbot does not understand a question or the company is not supported, it provides a helpful error message.

### Testing

The chatbot was tested using questions related to Microsoft, Tesla, and Apple.

It was also tested with greetings, help requests, and unsupported company queries.

The test results are included in `test_results.txt`.

### Limitations

- The chatbot supports only Microsoft, Tesla, and Apple.
- It supports fiscal years 2023–2025.
- It uses rule-based logic instead of advanced NLP.
- It cannot answer questions outside the included dataset.
- The financial data is static and is not connected to a live financial database.

### Data Unit

Financial values are expressed in USD millions.

### Conclusion

This prototype demonstrates how structured financial information can be transformed into an accessible conversational interface.

The prototype can later be extended with NLP, machine learning, live financial data integration, and a web-based interface.# BCG_GENAI_TASK2_CHATBOT
