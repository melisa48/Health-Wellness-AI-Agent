from datetime import datetime, timedelta
import random
from typing import List, Dict


class HealthWellnessAgent:
    def __init__(self, user_name: str):
        self.user_name = user_name
        self.user_data = {
            'fitness': {
                'workouts': [],
                'fitness_level': 'beginner',
                'goals': []
            },
            'mental_health': {
                'meditation_sessions': [],
                'mood_tracker': [],
                'stress_level': 'moderate'
            },
            'nutrition': {
                'meal_plan': [],
                'dietary_restrictions': [],
                'water_intake': []
            }
        }


class FitnessTrainer:
    def __init__(self):
        self.workout_types = {
            'beginner': {
                'cardio': [
                    {'name': 'Walking', 'duration': '30 mins', 'intensity': 'Low'},
                    {'name': 'Light jogging', 'duration': '20 mins', 'intensity': 'Low-Medium'},
                    {'name': 'Swimming', 'duration': '20 mins', 'intensity': 'Low-Medium'}
                ],
                'strength': [
                    {'name': 'Bodyweight squats', 'sets': 3, 'reps': '10-12'},
                    {'name': 'Push-ups on knees', 'sets': 3, 'reps': '8-10'},
                    {'name': 'Wall push-ups', 'sets': 3, 'reps': '12-15'}
                ],
                'flexibility': [
                    {'name': 'Basic stretches', 'duration': '10 mins'},
                    {'name': 'Yoga for beginners', 'duration': '15 mins'}
                ]
            },
            'intermediate': {
                # Similar structure for intermediate exercises
                'cardio': [{'name': 'Running', 'duration': '30 mins', 'intensity': 'Medium'}],
                'strength': [{'name': 'Regular push-ups', 'sets': 3, 'reps': '12-15'}],
                'flexibility': [{'name': 'Intermediate yoga', 'duration': '20 mins'}]
            },
            'advanced': {
                # Similar structure for advanced exercises
                'cardio': [{'name': 'Sprint intervals', 'duration': '30 mins', 'intensity': 'High'}],
                'strength': [{'name': 'Advanced calisthenics', 'sets': 4, 'reps': '15-20'}],
                'flexibility': [{'name': 'Advanced yoga', 'duration': '30 mins'}]
            }
        }

    def create_weekly_workout_plan(self, fitness_level: str, goals: List[str]) -> Dict:
        weekly_plan = {
            'Monday': self._create_daily_workout(fitness_level, 'Full Body'),
            'Tuesday': self._create_daily_workout(fitness_level, 'Cardio Focus'),
            'Wednesday': self._create_daily_workout(fitness_level, 'Full Body'),
            'Thursday': self._create_daily_workout(fitness_level, 'Cardio Focus'),
            'Friday': self._create_daily_workout(fitness_level, 'Full Body'),
            'Saturday': self._create_daily_workout(fitness_level, 'Light Activity'),
            'Sunday': {'type': 'Rest Day',
                       'description': 'Take time to rest and recover. Light stretching and walking are okay.'}
        }
        return weekly_plan

    def _create_daily_workout(self, fitness_level: str, focus: str) -> Dict:
        workout = {
            'exercises': [],
            'duration': 45,  # minutes
            'focus': focus,
            'notes': 'Remember to warm up for 5-10 minutes before starting and cool down afterwards.'
        }

        workout['exercises'].extend([
            random.choice(self.workout_types[fitness_level]['cardio']),
            random.choice(self.workout_types[fitness_level]['strength']),
            random.choice(self.workout_types[fitness_level]['flexibility'])
        ])

        return workout


class MentalHealthSupport:
    def __init__(self):
        self.meditation_exercises = {
            'beginner': {
                'Body scan': {
                    'description': 'A relaxation practice where you systematically focus attention on different parts of your body, from your feet to your head.',
                    'instructions': [
                        'Find a comfortable lying down position',
                        'Close your eyes and take several deep breaths',
                        'Start focusing on your toes, noticing any sensations',
                        'Gradually move your attention up through your body',
                        'Spend 20-30 seconds on each body part',
                        'End with focusing on your whole body as one unit'
                    ],
                    'benefits': [
                        'Reduces physical tension',
                        'Increases body awareness',
                        'Helps with stress management',
                        'Improves sleep quality'
                    ],
                    'duration': '10-15 minutes'
                },
                'Breathing awareness': {
                    'description': 'Simple meditation focusing on natural breath',
                    'instructions': [
                        'Sit comfortably with a straight back',
                        'Focus on your natural breathing pattern',
                        'Notice the sensation of air moving in and out',
                        'When mind wanders, gently return focus to breath'
                    ],
                    'benefits': [
                        'Reduces anxiety',
                        'Improves concentration',
                        'Calms the nervous system'
                    ],
                    'duration': '5-10 minutes'
                }
            },
            'intermediate': {
                'Mindful walking': {
                    'description': 'Walking meditation combining movement with awareness',
                    'instructions': [
                        'Choose a quiet path or space',
                        'Walk slowly and deliberately',
                        'Focus on the sensation of walking',
                        'Notice the movement of your body'
                    ],
                    'benefits': [
                        'Combines physical activity with meditation',
                        'Improves balance and coordination',
                        'Reduces anxiety while moving'
                    ],
                    'duration': '15-20 minutes'
                }
            }
        }

    def get_meditation_session(self, level: str, exercise_name: str) -> Dict:
        exercise = self.meditation_exercises[level][exercise_name]
        return {
            'exercise': exercise_name,
            'description': exercise['description'],
            'instructions': exercise['instructions'],
            'benefits': exercise['benefits'],
            'recommended_duration': exercise['duration']
        }


class NutritionAdvisor:
    def __init__(self):
        self.meal_options = {
            'vegan': {
                'breakfast': [
                    'Overnight oats with chia seeds and berries',
                    'Tofu scramble with vegetables',
                    'Smoothie bowl with plant-based protein'
                ],
                'lunch': [
                    'Quinoa buddha bowl with roasted vegetables',
                    'Chickpea and vegetable curry',
                    'Lentil and vegetable soup'
                ],
                'dinner': [
                    'Stir-fried tofu with vegetables',
                    'Black bean and sweet potato tacos',
                    'Mushroom and vegetable risotto'
                ],
                'snacks': [
                    'Mixed nuts and dried fruits',
                    'Hummus with vegetable sticks',
                    'Apple with almond butter'
                ]
            },
            'vegetarian': {
                'breakfast': [
                    'Greek yogurt parfait with granola',
                    'Vegetable omelette with cheese',
                    'Whole grain toast with avocado and eggs'
                ],
                'lunch': [
                    'Mediterranean pasta salad',
                    'Veggie and hummus wrap',
                    'Caprese sandwich'
                ],
                'dinner': [
                    'Eggplant parmesan',
                    'Black bean and quinoa burrito bowl',
                    'Vegetable stir-fry with tofu'
                ],
                'snacks': [
                    'Cheese and crackers',
                    'Trail mix',
                    'Yogurt with honey'
                ]
            },
            'omnivore': {
                'breakfast': [
                    'Oatmeal with fruits and nuts',
                    'Whole grain toast with eggs',
                    'Protein smoothie'
                ],
                'lunch': [
                    'Grilled chicken salad',
                    'Turkey wrap',
                    'Tuna sandwich'
                ],
                'dinner': [
                    'Baked salmon',
                    'Lean beef stir-fry',
                    'Grilled chicken with vegetables'
                ],
                'snacks': [
                    'Apple with almond butter',
                    'Protein bar',
                    'Greek yogurt'
                ]
            }
        }

    def create_meal_plan(self, dietary_preference: str, calories_target: int) -> Dict:
        if dietary_preference not in self.meal_options:
            dietary_preference = 'omnivore'  # default

        daily_meals = {
            'breakfast': random.choice(self.meal_options[dietary_preference]['breakfast']),
            'lunch': random.choice(self.meal_options[dietary_preference]['lunch']),
            'dinner': random.choice(self.meal_options[dietary_preference]['dinner']),
            'snacks': random.choice(self.meal_options[dietary_preference]['snacks'])
        }

        return {
            'dietary_type': dietary_preference,
            'meals': daily_meals,
            'total_calories': calories_target,
            'macros': self._calculate_macros(calories_target),
            'water_target': self._calculate_water_intake(weight_kg=70),
            'notes': self._get_dietary_notes(dietary_preference)
        }

    def _calculate_macros(self, calories: int) -> Dict:
        return {
            'protein': round(calories * 0.3 / 4),  # 4 calories per gram of protein
            'carbs': round(calories * 0.4 / 4),  # 4 calories per gram of carbs
            'fats': round(calories * 0.3 / 9)  # 9 calories per gram of fat
        }

    def _calculate_water_intake(self, weight_kg: float) -> float:
        return round(weight_kg * 30)  # Returns water intake in ml

    def _get_dietary_notes(self, preference: str) -> str:
        notes = {
            'vegan': 'Remember to supplement with B12 and consider tracking iron intake.',
            'vegetarian': 'Ensure adequate protein intake through eggs, dairy, and legumes.',
            'omnivore': 'Try to include a variety of protein sources and plenty of vegetables.'
        }
        return notes.get(preference, '')


def main():
    # Example usage
    agent = HealthWellnessAgent("John")

    # Create instances
    fitness_trainer = FitnessTrainer()
    mental_health = MentalHealthSupport()
    nutrition = NutritionAdvisor()

    # Generate plans
    workout_plan = fitness_trainer.create_weekly_workout_plan("beginner", ["weight loss"])
    meditation = mental_health.get_meditation_session("beginner", "Body scan")
    meal_plan = nutrition.create_meal_plan("vegan", 2000)

    # Print personalized plan
    print(f"Welcome {agent.user_name}! Here's your personalized health plan:\n")

    # Print workout plan
    print("Weekly Workout Plan:")
    for day, workout in workout_plan.items():
        print(f"\n{day}:")
        if day == "Sunday":
            print(f"- {workout['description']}")
        else:
            for exercise in workout['exercises']:
                duration = exercise.get('duration', '')
                sets = exercise.get('sets', '')
                reps = exercise.get('reps', '')
                if duration:
                    details = f"({duration})"
                else:
                    details = f"({sets} sets of {reps})"
                print(f"- {exercise['name']} {details}")

    # Print meditation details
    print("\nToday's Meditation: Body Scan")
    print("Description:", meditation['description'])
    print("Instructions:")
    for i, instruction in enumerate(meditation['instructions'], 1):
        print(f"{i}. {instruction}")
    print("\nBenefits:")
    for benefit in meditation['benefits']:
        print(f"- {benefit}")
    print(f"Recommended duration: {meditation['recommended_duration']}")

    # Print meal plan
    print("\nMeal Plan (Vegan):")
    for meal_type, meal in meal_plan['meals'].items():
        print(f"{meal_type.capitalize()}: {meal}")
    print(f"\nDietary Notes: {meal_plan['notes']}")
    print(f"Daily Water Target: {meal_plan['water_target']}ml")


if __name__ == "__main__":
    main()