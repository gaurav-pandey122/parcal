ORDER_STATUS = [
    ("pending", "Pending"),
    ("at_sorting", "At Sorting"),
    ("assigned", "Assigned for Delivery"),
    ("at_delivery_hub", "At Delivery Hub"),
    ("transit", "In Transit"),
    ("hold", "on Hold"),
    ("cancelled", "Cancelled"),
    ("delivery", "Delivery"),
    ("partial_delivery", "Partial Delivery"),
    ("exchange", "Exchange"),
    ("returned", "Returned"),
    ("paid_return", "Paid Return"),
    ("return_transit", "Return In Transit"),
    ("return_at_sorting", "Return At Sorting"),
    ("return_assigned", "Assigned for Return"),
    ("first_mile_hub", "First Mile Hub"),
    ("return_to_merchant", "Return To Merchant"),
]

ORDER_STAGE = [
    ("active", "Active"),
    ("delivered", "Delivered"),
    ("returned", "Returned"),
    ("reverse_delivery", "Reverse Delivery"),
]

WEIGHT_CHOICES = [
    ("0-0.2", "0-0.2"),
    ("0.2-0.5", "0.2-0.5"),
    ("0.5-1", "0.5-1"),
    ("1-1.5", "1-1.5"),
    ("1.5-2", "1.5-2"),
    ("2-3", "2-3"),
    ("3-4", "3-4"),
    ("4-6", "4-6"),
    ("6-7", "6-7"),
    ("7-8", "7-8"),
    ("8-9", "8-9"),
    ("9-10", "9-10"),
    ("10-11", "10-11"),
    ("11-12", "11-12"),
    ("12-13", "12-13"),
    ("13-14", "13-14"),
    ("14-15", "14-15"),
]


def order_status(order):
    status = ORDER_STATUS[order.status]
    return status


def order_stage(order):
    stage = ORDER_STAGE[order.status]
    return stage
