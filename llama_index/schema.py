# ... existing code ...

class BaseNode(BaseComponent):
    # ... existing code ...

    @property
    def node_id(self) -> str:
        return self.id_

    @node_id.setter
    def node_id(self, new_id: str) -> None:
        # Add any validation rules for new_id here if necessary
        self.id_ = new_id

    # ... existing code ...