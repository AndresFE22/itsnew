import mysql.connector
from mysql.connector import connect, Error


class IntelligentTutor:
    def __init__(self):
        self.student_progress = 0
        self.current_activity = 0
        self.activities = [
            "Activity 1: Identify Climate Change Factors",
            "Activity 2: Plan Energy Conservation Strategy",
            "Activity 3: Reduce Plastic Usage"
        ]
    
    def start_tutorial(self):
        print("Welcome to the Intelligent Tutor System!")
        print("Let's develop your probtemplates/activity/High/Global/Activo/activity1lem-solving skills related to climate change.")
        self._display_activity()
    
    def _display_activity(self):
        if self.current_activity < len(self.activities):
            print("\nCurrent Activity:", self.activities[self.current_activity])
            self._provide_guidance()
        else:
            print("\nCongratulations! You've completed all activities.")
    
    def _provide_guidance(self):
        
        activity_info = {
            0: "Analyze different factors contributing to climate change.",
           #1: "Plan a strategy to reduce energy consumption at home.",
            #2: "Devise a plan to minimize plastic usage in your daily life."
        }
        
        print("Guidance:", activity_info.get(self.current_activity, "No guidance available."))
        self._simulate_student_interaction()
    
    def _simulate_student_interaction(self):
        print("Simulating student interaction...")
        # Here, you can simulate the student's decisions and actions.
        # You would provide feedback based on their choices and update progress.
        self.student_progress += 10
        self.current_activity += 1
        self._display_activity()
        
        
        
        
class LearningGoals:
    def __init__(self):
        self.goals = {
            "PrepositionOfTime": {
                "levels": {
                    "low": [
                        {"name": "PrepositionOfTimeLow1", "completed": False}                      
                    ],
                    "medium": [
                        {"name": "PrepositionOfTimeMedium2", "completed": False},
                    ],
                    "high": [
                        {"name": "PrepositionOfTimeHigh3", "completed": False},
                    ]
                }
            },

            "PrepositionOfPlace": {
                "levels": {
                    "low": [
                        {"name": "PrepositionOfPlaceLow4", "completed": False},
                    ],
                    "medium": [
                        {"name": "PrepositionOfPlaceMedium5", "completed": False},
                    ],
                    "high": [
                        {"name": "PrepositionOfPlaceHigh6", "completed": False},
                    ]
                }
            },

            "PrepositionOfMovement": {
                "levels": {
                    "low": [
                        {"name": "PrepositionOfMovementLow7", "completed": False},
                    ],
                    "medium": [
                        {"name": "PrepositionOfMovementMedium8", "completed": False},
                    ],
                    "high": [
                        {"name": "PrepositionOfMovementHigh9", "completed": False},
                    ] 
                }
            }
        }  
    
    def mark_activity_completed(self, activity_name):
        for goal in self.goals.values():
            for level_activities in goal["levels"].values():
                for activity in level_activities:
                    if activity["name"] == activity_name:
                        activity["completed"] = True
    
    def recommend_learning_path(self, order_array):
        recommended_path = []
        valid_goals = [goal for goal in order_array if goal in self.goals]

        for goal_name in valid_goals:
            goal_data = self.goals[goal_name]

            for level_name, level_activities in goal_data["levels"].items():
                for activity in level_activities:
                    if not activity["completed"]:
                        recommended_path.append({
                            "goal": goal_name,
                            "lvl": level_name,
                            "name": activity["name"]
                    })

    # Construir el resultado en el orden de order_array
        print(recommended_path)
        result_in_order = []
        for goal_name in order_array:
            for activity in recommended_path:
                if activity["goal"] == goal_name:
                    result_in_order.append(activity)
                    print(result_in_order)
        return result_in_order

    
    def print_learning_goals(self):
        print("Learning Goals:")
        for goal_name, goal_data in self.goals.items():
            print(f"- {goal_name}:")
            for level, level_activities in goal_data["levels"].items():
                print(f"  {level} lvl:")
                for activity in level_activities:
                    status = "Completed" if activity["completed"] else "Not Completed"
                    print(f"    {activity['name']}: {status}")
            print()


    def calculate_learning_style_score(self, selected_styles):
        styles_data = {
            'perception': {
                'Activo': 0,
                'Reflexivo': 0
        },
            'processing': {
                'Sensorial': 0,
                'Intuitivo': 0
        },
            'reception': {
                'Visual': 0,
                'Verbal': 0
        },
            'navigation': {
                'Secuencial': 0,
                'Global': 0
        },
    }

        results = []

        for question, data in selected_styles.items():
            style, response = data['style'], data['response']
            first_style, second_style = style.split('/')
            styles_key = None
        
            if 'Activo' in style and 'Reflexivo' in style:
                styles_key = 'perception'
            elif 'Sensorial' in style and 'Intuitivo' in style:
                styles_key = 'processing'
            elif 'Visual' in style and 'Verbal' in style:
                styles_key = 'reception'
            elif 'Secuencial' in style and 'Global' in style:
                styles_key = 'navigation'
        
            if styles_key is not None:
                if response == 'a':
                    styles_data[styles_key][first_style] += 1
                elif response == 'b':
                    styles_data[styles_key][second_style] += 1
    
        for style_key, style_scores in styles_data.items():
            style_difference = max(style_scores.values()) - min(style_scores.values())
            dominant_style = max(style_scores, key=style_scores.get)
            results.append({'style': style_key, 'dominant_style': dominant_style, 'subtraction': style_difference})
            
        return results
    

    
class LearningResource:
    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            print("Connected to database successfully")
            self.cursor = self.connection.cursor(buffered=True)
        except mysql.connector.Error as err:
            print("Error connecting to database:", err)
                

    
    def find_resource(self, recommended_path, combined_styles):
        results = []
        pt_values = []
        

        for entry in recommended_path:
            name = entry['name']
            goal = entry['goal']
            lvl = entry['lvl']
            query = (
                "SELECT url, pt, lc FROM learningresourcesimplified "
                "WHERE name= %s AND goal= %s AND lvl= %s"
            )
            print("voy por las de", name, goal, lvl)
            values = (name, goal, lvl)
            self.cursor.execute(query, values)
            results_for_entry = self.cursor.fetchall()
            print('result', results_for_entry)

            for result in results_for_entry: 
                url, pt, lc = result
                resource_info = {
                    "name": name,
                    "goal": goal,
                    "lvl": lvl,
                    "url": url,
                    "pt": pt,
                    "lc": lc
            }
                results.append(resource_info)
            else:
            
                print("No resource found for:", name, goal, lvl)
        
        combined_style_values = [(style, dominant_style) for style, dominant_style in (cs.split(': ') for cs in combined_styles)]

        for combined_style_value in combined_style_values:
            style, dominant_style = combined_style_value
            pt_values.append(dominant_style)

        style_query = (
            "SELECT pt FROM learningstylesimplified "
            "WHERE perception = %s AND processing = %s AND reception = %s"
        )

        values_styles = (pt_values[1], pt_values[0], pt_values[2])
        print("values styles", values_styles)
        self.cursor.execute(style_query, values_styles)
        results_style_for_entry = self.cursor.fetchall()
        print("result", results_style_for_entry)

        
        if not results_style_for_entry:
        # Si no se encuentran coincidencias con los tres valores,
        # Intentamos encontrar coincidencias con al menos dos de ellos.
            style_query = (
            "SELECT pt FROM learningstylesimplified "
            "WHERE (perception = %s AND processing = %s) OR "
            "(perception = %s AND reception = %s) OR "
            "(processing = %s AND reception = %s) LIMIT 1"
    )
            
            values_styles = (pt_values[1], pt_values[0], pt_values[0], pt_values[2], pt_values[2], pt_values[1])
            self.cursor.execute(style_query, values_styles)
            results_style_for_entry = self.cursor.fetchall()

            if not results_style_for_entry:
            # Si no se encuentran coincidencias con al menos dos valores,
            # buscamos coincidencias basadas en el primer valor que se encuentre.
                style_query = "SELECT pt FROM learningstylesimplified WHERE perception = %s LIMIT 1"
                self.cursor.execute(style_query, (pt_values[0],))
                results_style_for_entry = self.cursor.fetchall()

        print('pedagogic_tactic:', pt_values)
        style_result_flat = [item[0] for item in results_style_for_entry]
        print('flat', style_result_flat)


        filtered_styles = [resource for resource in results if resource['pt'] in style_result_flat]

        level_order = {'low': 0, 'medium': 1, 'high': 2}
        ordered_resources = sorted(filtered_styles, key=lambda x: level_order[x['lvl']])



        print("Final resources", ordered_resources)

        return ordered_resources
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

class authenticated:
    def __init__(self) -> None:
        pass
        
    def is_authenticated(self, username):
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="its"
            ) as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM student WHERE user = %s"
                cursor.execute(query, (username,))
                user = cursor.fetchone()
                return user is not None
        except Error as e:
            print("Error:", e)
            return False
      
        
        

# Main program
if __name__ == "__main__":
    tutor = IntelligentTutor()
    tutor.start_tutorial()
    learning_goals = LearningGoals()
    learning_goals.recommend_learning_path()
    learning_goals.print_learning_goals()
    Learning_Resource = LearningResource()
    Learning_Resource.find_resource











