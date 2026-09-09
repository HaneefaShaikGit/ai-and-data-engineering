# AI in Data Engineering: Assistant, Not Autopilot

I've been thinking a lot about where AI actually fits into data engineering.

When people talk about AI and software jobs, the discussion quickly turns into whether AI will replace engineers. From what I've seen while working with data pipelines and while using AI myself, I think that's the wrong question.

AI can definitely make a data engineer faster. I use it to understand unfamiliar code, think through SQL, document ideas and sometimes get a second opinion when debugging. But there is a big difference between generating code and knowing whether that code is correct for the business.

A model can write a JOIN in seconds. It doesn't automatically know whether that JOIN breaks the grain of a fact table.

## What AI is good at

AI is useful for repetitive, text-heavy, and pattern-based work:

- generating a first draft of SQL
- explaining unfamiliar code
- drafting documentation
- suggesting dbt tests
- summarizing logs
- generating boilerplate Airflow or PySpark code

The important word is **suggesting**.

## Where engineering judgment still matters

A model can generate a JOIN:

```sql
SELECT *
FROM claims c
JOIN policies p
  ON c.policy_id = p.policy_id
```

But a data engineer still has to ask:

- Is `policy_id` unique?
- Is the policy table SCD Type 2?
- Should the claim join to the current or historical policy row?
- Can the JOIN duplicate claims?
- Is the business asking for current-state or point-in-time reporting?

These are modeling and business questions, not just coding questions.

## AI can generate code faster than it can understand context

A generated transformation may be syntactically correct and still be wrong.

For example:

```sql
SELECT
    customer_id,
    SUM(claim_amount) AS total_claim_amount
FROM claims
GROUP BY customer_id
```

What if rejected claims should be excluded? What if currencies differ? What if the source is transaction-grain and duplicates claims?

The model needs context.

## AI makes metadata more valuable

Useful metadata includes:

- table descriptions
- column definitions
- business keys
- model grain
- lineage
- SLA information
- data quality rules
- ownership

Without metadata, an AI assistant is guessing.

## AI for data quality

Traditional rules are deterministic:

```text
customer_id IS NOT NULL
claim_amount >= 0
policy_start_date <= policy_end_date
```

AI/ML can complement them by spotting unusual patterns:

- row count suddenly drops
- runtime increases sharply
- null percentage jumps
- source arrival time starts drifting

That is where anomaly detection can help.

## My current opinion

The strongest data engineers in an AI-heavy environment will not be the people who avoid AI.

They also will not be the people who blindly copy whatever AI generates.

They will be the engineers who can:

1. define the problem clearly
2. provide the right context
3. evaluate the output
4. understand the underlying system
5. validate the result
6. take responsibility for production behavior

That got me curious about another use case: instead of asking AI to generate pipelines, could we use ML to help observe them?
So I built a tiny experiment.

## Key Takeaway

> AI is most useful when it acts as an engineering assistant, not an engineering authority.
