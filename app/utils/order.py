ACTIVE_ORDER_STATUS = [
    ("pending", "Pending"),
    ("assigned", "Assigned for Delivery"),
    ("transit", "In Transit"),
    ("hold", "on Hold"),
]

DELIVERY_ORDER_STATUS = [
    ("delivery", "Delivery"),
    ("partial_delivery", "Partial Delivery"),
    ("exchange", "Exchange"),
]
RETURN_ORDER_STATUS = [
    ("returned", "Returned"),
    ("paid_return", "Paid Return"),
]
REVERSE_ORDER_STATUS = [
    ("return_transit", "Return In Transit"),
    ("return_assigned", "Assigned for Return"),
    ("return_to_merchant", "Return To Merchant"),
]

ORDER_STAGE = [
    ("active", "Active"),
    ("delivered", "Delivered"),
    ("returned", "Returned"),
    ("reverse_delivery", "Reverse Delivery"),
]

ORDER_STATUS = (
    ACTIVE_ORDER_STATUS
    + DELIVERY_ORDER_STATUS
    + RETURN_ORDER_STATUS
    + REVERSE_ORDER_STATUS
    + [
        ("cancelled", "Cancelled"),
    ]
)

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


def state_status(state):
    if state == "active":
        return ACTIVE_ORDER_STATUS
    elif state == "delivered":
        return DELIVERY_ORDER_STATUS
    elif state == "returned":
        return RETURN_ORDER_STATUS
    elif state == "reverse_delivery":
        return REVERSE_ORDER_STATUS
    else:
        return ORDER_STATUS


def order_stage(state):
    ORDER_STAGE_DICT = dict(ORDER_STAGE)
    if state == "all":
        return ("all", "All")

    value = ORDER_STAGE_DICT.get(state, "Unknown")
    return (state, value)
