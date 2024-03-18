# Copyright (c) 2024, Applied Relevance and contributors
# For license information, please see license.txt

from frappe.model.document import Document

class Contribution(Document):
    def before_save(self):
        if self.unit == "Hours":
            self.points = self.value * self.fhrr * self.point_conversion_rate
        elif self.unit == "Cash":
            self.points = self.value * self.point_conversion_rate
        elif self.unit == "Resources":
            # Assuming resources are valued similarly to cash contributions
            self.points = self.value * self.point_conversion_rate
        else:
            self.points = 0
