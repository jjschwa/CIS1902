---
layout: page
title: Staff
description: A listing of all the course staff members.
---

# Staff

The best way to contact staff is by posting on the EdStem. Private posts can be viewed by all 3 staff members. You are likely to get a quicker response by posting there. If you have a private question, please reach out to the instructor, Jordan.

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{% assign teaching_assistants = site.staffers | where: 'role', 'Teaching Assistant' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}
## Teaching Assistants

{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}
