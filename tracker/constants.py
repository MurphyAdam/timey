STATUSES = (
    ('UNVERIFIED', 'Unverified'),
    ('VERIFIED', 'Verified'),
    ('APPROVED', 'Approved'),
    ('INVOICED', 'Invoiced'),
    ('NOT_INVOICED', 'Not Invoiced'),
)

TIMER_STATE = (
    ('paused', 'pause'),
    ('running', 'run'),
    ('toggle', 'toggle'),
)


class TIMER_ACTION():
    PAUSE = 'paused'
    UNPAUSE = 'running'
    TOGGLE = 'toggle'
