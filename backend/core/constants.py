CONTACT_NUMBER_REGEX = r'^\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'


class Action:
    CREATE = "create"
    DESTROY = "destroy"
    LIST = "list"
    PARTIAL_UPDATE = "partial_update"
    RETRIEVE = "retrieve"
    UPDATE = "update"


class DateTimeFormat:
    DATE_TIME = "%d-%m-%Y %H:%M"
    DATE = "%d-%m-%Y"
    TIME = "%H:%M"
