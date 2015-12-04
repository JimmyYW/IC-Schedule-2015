from app.models import Course, SectionToTime, Time, Section

"""
ALGORITHM
1. Create a dictionary of dictionary of lists (course to section to times)
2. Do a double loop to compare classes: i = (0, len(dict.keys())-1) and j = (i, len(dict.keys())
3. Each loop goes from 0 to len(dict[coursename]).keys())-1 (i.e. num of sections)
4. Compare times for sections.
    - If there are no conflicts, add a tuple of sections to a list???
        - FOR NOW: Just break and display one schedule that works, you nincompoop.
    - If there are conflicts, continue.
5. At the end of the outer loop, you have a shit.

TAKE TWO

1. Still with the dictionary of dictionaries of lists. I think.
2. Pick the first section from each.
    -If it time work, display it
    -If it don't, don't
3. Increment a section, rinse, repeat

Comparing and looping with an unknown number of classes is going to be tricky, but I'm going to launch right in.
"""


def make_selected_dict(courses):
    selected = dict()
    for c in courses:
        sections = Section.query.filter_by(courseId=c.id)
        selected[c] = list()
        for s in sections:
            s2ts = SectionToTime.query.filter_by(sectionId=s.id)
            times = list()
            for s2t in s2ts:
                times.append(Time.query.get(s2t.timeId))
            selected[c].append({s: times})
    return selected


selected = make_selected_dict(Course.query.all())
print(selected)

