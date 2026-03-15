# test_tags.py
from metaflow import FlowSpec, step, current

class TagsTestFlow(FlowSpec):
    @step
    def start(self):
        print("Tags:", current.tags)
        assert current.tags is not None
        self.next(self.end)
    
    @step
    def end(self):
        pass

if __name__ == "__main__":
    TagsTestFlow()
