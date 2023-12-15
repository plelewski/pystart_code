import json
from datetime import datetime, timedelta


class Meeting:
    def __init__(self, start_time: datetime, title: str):
        self.start_time = start_time
        self.end_time = start_time + timedelta(hours=1)
        self.title = title


class Calendar:
    def __init__(self):
        self.meetings = {}

    def check_if_is_free(self, event_at: datetime):
        return event_at not in self.meetings

    def add_meeting(self, meeting: Meeting):
        self.meetings[meeting.start_time] = meeting

    def show_meetings(self, day: datetime = None):
        if day is None:
            return self.meetings

        events = []
        for event in self.meetings.values():
            if event.start_time.date() == day.date():
                events.append(event)

        return events

    # def add_to_json_file(self, ev: list):
    #     with open('meetings.json', encoding='utf8', mode='w') as jsonfile:
    #         json.dump(ev, jsonfile)


if __name__ == '__main__':
    m1 = Meeting(datetime(2023, 11, 22, 9), 'Daily')
    m2 = Meeting(datetime(2023, 12, 2, 10), 'One on One')
    m3 = Meeting(datetime(2023, 12, 1, 12), 'Two on two')
    m4 = Meeting(datetime(2023, 12, 3, 14), 'Update call')

    cal = Calendar()
    cal.add_meeting(m1)
    cal.add_meeting(m2)
    cal.add_meeting(m3)
    cal.add_meeting(m4)

    events = cal.show_meetings()
    # cal.add_to_json_file(events)
