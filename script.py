import ast
import os
import re

file_names = os.listdir('./logs')

for file_name in file_names:
	if 'MLP_RandomOverSampler' in file_name or 'MLP_SMOTE.txt' in file_name:
		file = open('./logs/' + file_name, 'r', encoding = 'utf-8')
		hyperparameters = ast.literal_eval(file.readline())
		# for key, val in hyperparameters.items():
		# 	#\\\\ \\hline
		# 	key = key.replace('_', '\\_')
		# 	if isinstance(val, str) and '_' in val:
		# 		val = val.replace('_', '\\_')
		# 	print(key+" & "+str(val)+" \n\\\\ \\hline")
		print("\n\\begin{table}[H]\n\\centering\n\\resizebox{\\textwidth}{!}{\n    \\begin{tabular}{|c|c|c|c|}")
		file.readline()
		print("    \\hline\n        \\textbf{Metric} & \\textbf{Score Mean} & \\textbf{Score Variance} & \\textbf{Score Std}", end='')
		for i in range(0, 7):
			s = re.split(" +", file.readline())
			# print(s)
			print("\n    \\\\ \\hline", end='\n        ')
			for token in s[:-1]:
				print(token, end='')
				if token != s[-2]:
					print(' & ', end='')
		print("\n    \\\\ \\hline\n    \\end{tabular}\n}\n\\caption{Risultati delle metriche di valutazione per i "+file_name+"}\n\\label{tab:dt_val1}\n\\end{table}")
