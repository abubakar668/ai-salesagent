def generate_prompt(product_name, company_url, product_category, competitors, value_proposition, target_customer):
    return f"""
    Analyze the following information and provide a structured report with the specified headings:

    Product Name: {product_name}
    Company URL: {company_url}
    Product Category: {product_category}
    Competitors: {competitors}
    Value Proposition: {value_proposition}
    Target Customer: {target_customer}

    Please structure the response with the following sections:
    1. **Company Strategy** - Include a summary of the company's activities in the industry relevant to the product, mention any public statements, press releases, or articles by key executives such as the Chief Data Officer or Chief Compliance Officer, and summarize job postings or other indicators of company strategy or technology stack.
    2. **Competitor Mentions** - Discuss any mention of the competitors provided in the input.
    3. **Leadership Information** - Provide information on key leaders at the prospect company and their relevance, especially those quoted in press releases over the last year.
    4. **Product/Strategy Summary** - For public companies, include insights from 10-Ks, annual reports, or other relevant documents available online.
    5. **Article Links** - Provide links to full articles, press releases, or other sources mentioned in the output.
    """