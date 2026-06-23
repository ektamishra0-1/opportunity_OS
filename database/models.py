class Observation:
    def __init__(
        self,
        source,
        source_id,
        title,
        content,
        author,
        url,
        timestamp
    ):
        self.source = source
        self.source_id = source_id
        self.title = title
        self.content = content
        self.author = author
        self.url = url
        self.timestamp = timestamp

class Problem:
    def __init__(
        self,
        observation_title,
        problem_text,
        category,
        confidence
    ):
        self.observation_title = observation_title
        self.problem_text = problem_text
        self.category = category
        self.confidence = confidence