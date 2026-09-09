from inspect_ai.log import read_eval_log, list_eval_logs
log = read_eval_log(list_eval_logs('./logs')[0].name)
for s in log.samples:
    inp = s.input if isinstance(s.input, str) else s.input[-1]['content']
    sc = list(s.scores.values())[0]
    print(f"[{'OK ' if sc.value else 'MISS'}] gold={s.target} said={sc.answer} :: {inp[:80]}")
