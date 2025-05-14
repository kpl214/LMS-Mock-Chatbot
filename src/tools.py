import pandas as pd
from langchain.tools import tool
grades_df = pd.read_csv("grades.csv")
topics_df = pd.read_csv("coursecontent.csv")

@tool
def get_current_grade(course: str) -> str:
    """Return the weighted average grade for a given course name."""
    #used as function description for llm
    course_data = grades_df[grades_df["course"].str.lower() == course.lower()]
    if course_data.empty:
        return "Course not found"

    # g1*w1 + g2*w2 + ... / w1 + w2 + ...
    weighted_sum = (course_data["grade"] * course_data["weight"]).sum()
    total_weight = course_data["weight"].sum()

    weighted_average = weighted_sum / total_weight
    return f"{round(weighted_average, 2)}"

@tool
def get_course_topics(course: str) -> str:
    """Return a comma seperated list of course topics and their dates."""
    topics = topics_df[topics_df["course"].str.lower() == course.lower()]
    if topics.empty:
        return "No topics found for this course"

    formatted = [f"{row['topic']} ({row['date']})" for _, row in topics.iterrows()]
    return ", ".join(formatted)