"""
Master Question Dataset Builder and Validator for Online CSE Quiz System.
Compiles and verifies all 500 questions into `questions.json`.
"""

import json
import os
import sys

from data_builder.cat1_prog_fund import QUESTIONS as Q1
from data_builder.cat2_python import QUESTIONS as Q2
from data_builder.cat3_ds import QUESTIONS as Q3
from data_builder.cat4_algo import QUESTIONS as Q4
from data_builder.cat5_dbms import QUESTIONS as Q5
from data_builder.cat6_os import QUESTIONS as Q6
from data_builder.cat7_cn import QUESTIONS as Q7
from data_builder.cat8_coa import QUESTIONS as Q8
from data_builder.cat9_se import QUESTIONS as Q9
from data_builder.cat10_web import QUESTIONS as Q10
from data_builder.cat11_ai_ml import QUESTIONS as Q11
from data_builder.cat12_cyber import QUESTIONS as Q12

EXPECTED_DISTRIBUTION = {
    "Programming Fundamentals": (Q1, 50),
    "Python Programming": (Q2, 50),
    "Data Structures": (Q3, 50),
    "Algorithms": (Q4, 50),
    "DBMS": (Q5, 50),
    "Operating Systems": (Q6, 50),
    "Computer Networks": (Q7, 50),
    "Computer Organization & Architecture": (Q8, 40),
    "Software Engineering": (Q9, 30),
    "Web Technologies": (Q10, 30),
    "Artificial Intelligence & Machine Learning Basics": (Q11, 25),
    "Cyber Security": (Q12, 25)
}

def build_dataset():
    all_questions = []
    seen_questions = set()
    current_id = 1
    
    diff_counts = {"Easy": 0, "Medium": 0, "Hard": 0}

    for cat_name, (q_list, target_count) in EXPECTED_DISTRIBUTION.items():
        actual_count = len(q_list)
        print(f"Checking '{cat_name}': target={target_count}, actual={actual_count}")
        if actual_count != target_count:
            raise ValueError(f"Category '{cat_name}' has {actual_count} questions; expected {target_count}")
        
        for q in q_list:
            q_text = q["question"].strip()
            if q_text in seen_questions:
                raise ValueError(f"Duplicate question detected in '{cat_name}': {q_text}")
            seen_questions.add(q_text)

            diff = q["difficulty"]
            if diff not in diff_counts:
                raise ValueError(f"Invalid difficulty '{diff}' for question: {q_text}")
            diff_counts[diff] += 1

            options = q["options"]
            if not isinstance(options, list) or len(options) != 4:
                raise ValueError(f"Question must have exactly 4 options. Got {options} for: {q_text}")
            
            # Check unique options
            if len(set(options)) != 4:
                raise ValueError(f"Options must be distinct for question: {q_text}, got {options}")
            
            answer = q["answer"]
            if answer not in options:
                raise ValueError(f"Answer '{answer}' not found in options {options} for: {q_text}")
            
            explanation = q.get("explanation", "").strip()
            if not explanation:
                raise ValueError(f"Explanation missing for question: {q_text}")
            
            all_questions.append({
                "id": current_id,
                "category": cat_name,
                "difficulty": diff,
                "question": q_text,
                "options": options,
                "answer": answer,
                "explanation": explanation
            })
            current_id += 1

    total = len(all_questions)
    print(f"\n==========================================")
    print(f"Total Questions Verified: {total} (Target: 500)")
    print(f"Difficulty Breakdown:")
    for d, c in diff_counts.items():
        print(f"  - {d}: {c} ({c / total * 100:.1f}%)")
    print(f"==========================================")

    if total != 500:
        raise ValueError(f"Total questions count is {total}, expected exactly 500!")

    output_path = os.path.join(os.path.dirname(__file__), "questions.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully generated '{output_path}' with {total} questions.")

if __name__ == "__main__":
    build_dataset()
