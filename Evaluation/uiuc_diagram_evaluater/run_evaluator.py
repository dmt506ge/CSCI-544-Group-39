import os
import sys
# script running program
def run_program(model):
    ground_path = "../ground_png"
    eval_path = f"../evaluate_png/{model}"
    output_path = f"../eval_output/{model}"
    for f in os.listdir(eval_path):
        if f.endswith(".png"):
            eval_run_path = eval_path + "/" + f
            ground_run_path = ground_path+"/"+f
            runargu = f"python script/evaluate_diagram.py {eval_run_path} {ground_run_path} --output-dir {output_path}"
            os.system(runargu)

if __name__ == "__main__":
    run_program(sys.argv[1])