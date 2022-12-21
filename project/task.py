class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if self.name == new_name:
            return f'Name cannot be the same.'

        self.name = new_name
        return self.name

    def change_due_date(self, new_due_date):
        if self.due_date == new_due_date:
            return 'Date cannot be the same'

        self.due_date = new_due_date
        return self.due_date

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_idx, new_comment):
        if comment_idx < 0 or comment_idx >= len(self.comments):
            return f'Cannot find comment'

        self.comments[comment_idx] = new_comment
        return ', '.join(self.comments)

    def details(self):
        return f'Name: {self.name} - Due date: {self.due_date}'