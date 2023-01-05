class ExercisePlan:
    id = 1

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()

    @staticmethod
    def get_next_id():
        res = ExercisePlan.id
        ExercisePlan.id += 1
        return res

    def __repr__(self):
        return f'Plan <{self.id}> with duration {self.duration} minutes'
