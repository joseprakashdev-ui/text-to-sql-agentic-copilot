"""Self-Healing Text-to-SQL Agent."""
import re

class TextToSQLCopilot:
    FORBIDDEN_KEYWORDS = ["DROP", "DELETE", "TRUNCATE", "ALTER", "GRANT", "UPDATE", "INSERT"]

    @classmethod
    def validate_safety(cls, sql_query: str) -> bool:
        """Enforces strictly read-only execution."""
        for kw in cls.FORBIDDEN_KEYWORDS:
            if re.search(rf"\b{kw}\b", sql_query, re.I):
                raise PermissionError(f"Security Alert: Destructive query keyword '{kw}' detected.")
        return True

    @classmethod
    def format_query(cls, natural_query: str) -> str:
        """Translates intent to standardized SQL with automatic schema guardrails."""
        # Simulated generator
        return "SELECT SUM(LOAN_AMOUNT) AS TOTAL_EXPOSURE FROM LOANS WHERE STATUS = 'ACTIVE' AND DSCR < 1.25;"

if __name__ == "__main__":
    sample = "Show total exposure for subprime loans"
    sql = TextToSQLCopilot.format_query(sample)
    if TextToSQLCopilot.validate_safety(sql):
        print("Generated Safe SQL:", sql)
