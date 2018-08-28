import json
import numpy as np

path = r"d:\GitRoot\VirtualSeller\TC-Bot\src\deep_dialog\checkpoints\rl_agent\my_noe2e\agt_9_performance_records.json"
#path = r"d:\GitRoot\VirtualSeller\TC-Bot\src\deep_dialog\checkpoints\rl_agent\my_e2e\agt_9_performance_records.json"

data = json.load(open(path, 'rb'))
ave_turn_list = [data["ave_turns"][str(i)] for i in range(len(data["ave_turns"]))]
success_rate_list = [data["success_rate"][str(i)] for i in range(len(data["ave_turns"]))]
ave_reward_list = [data["ave_reward"][str(i)] for i in range(len(data["ave_turns"]))]

n_rerun = 0
best = -1.
for cur_success_rate in success_rate_list:
    if cur_success_rate >= best:
        if cur_success_rate >= 0.3:
            n_rerun += 1
        best = cur_success_rate

print(n_rerun)
print(np.average(ave_turn_list))