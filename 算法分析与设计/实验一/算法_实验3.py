def parse_time(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s
    # 转化到具体的秒数，时间冲突算法简单

def max_reward_jobs(jobs):

    jobs.sort(key=lambda x: x[3])

    n = len(jobs)
    dp = [0] * n
    dp[0] = jobs[0][1]

    job_selection = [[] for _ in range(n)]
    job_selection[0].append(jobs[0][0])

    for i in range(1, n):
        include_reward = jobs[i][1]
        for j in range(i - 1, -1, -1):
            if jobs[j][3] <= jobs[i][2]: #
                include_reward += dp[j]
                break
        # 判断时间是否冲突
        if include_reward > dp[i - 1]:
            dp[i] = include_reward
            if j >= 0 and jobs[j][3] <= jobs[i][2]:
                job_selection[i] = job_selection[j] + [jobs[i][0]]
            else:
                job_selection[i] = [jobs[i][0]]
        else:
            dp[i] = dp[i - 1]
            job_selection[i] = job_selection[i - 1]

    max_reward = dp[-1]
    max_jobs = set(job_selection[-1])
    return max_jobs, max_reward

n = int(input("工作的数量："))
jobs = []
for _ in range(n):
    job_id, reward, start_time, end_time = (input().split())
    jobs.append((int(job_id), int(reward), parse_time(start_time), parse_time(end_time)))

job_set, total_reward = max_reward_jobs(jobs)
print(f"选择任务为：{job_set}")
print(f"最大酬劳为：{total_reward}")
