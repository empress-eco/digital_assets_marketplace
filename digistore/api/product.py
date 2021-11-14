import frappe

from typing import List


@frappe.whitelist()
def all_products() -> List:
	return frappe.db.get_all(
		"Product",
		filters={"available": True},
		fields=["name", "image", "title", "description", "category", "short_description"],
	)


@frappe.whitelist()
def purchased(user: str = None) -> List:
	user_products = []

	if not user:
		user = frappe.session.user

	user_purchases = frappe.get_all(
		"Store Purchase", filters={"purchased_by": user}, fields=["product", "plan"]
	)

	for purchase in user_purchases:
		product = frappe.get_doc("Product", purchase.product)
		plan = frappe.get_doc("Plan", purchase.plan)

		user_products.append({"product": product, "plan": plan})

	return user_products