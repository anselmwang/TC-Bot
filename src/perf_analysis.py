import pstats
p = pstats.Stats(r"d:\GitRoot\VirtualSeller\TC-Bot\src\deep_dialog\checkpoints\rl_agent\my_noe2e_speedup\stats.noe2e_train")
#p = pstats.Stats(r"d:\GitRoot\VirtualSeller\TC-Bot\src\deep_dialog\checkpoints\rl_agent\my_noe2e\stats.noe2e_train")
p.sort_stats('cumulative').print_stats(20)


