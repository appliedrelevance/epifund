# Copyright (c) 2024, Applied Relevance and contributors
# For license information, please see license.txt

from frappe.model.document import Document

class FounderPosition(Document):
    def before_save(self):
        if self.salary_basis == "Annual" and self.market_salary:
            self.hourly_rate = self.market_salary / 2080
