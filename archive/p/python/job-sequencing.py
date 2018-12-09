#!/usr/bin/env python
import argparse


class Job:
    def __init__(self, profit, deadline):
        self.profit = profit
        self.deadline = deadline

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __gt__(self, other):
        return self.profit > other.profit

    def __lt__(self, other):
        return self.profit < other.profit


def input_list(list_str):
    return [int(x.strip(" "), 10) for x in list_str.split(',')]


def max_profit(jobs):
    return sum([j.profit for _, j in iterate_job_sequence(jobs).items()])


def iterate_job_sequence(available, complete=None):
    complete = complete or {}
    if not available:
        return complete
    max_job = max(available)
    available.remove(max_job)
    index_opts = [i for i in range(0, max_job.deadline) if i not in complete]
    new_index = max(index_opts) if index_opts else -1
    if new_index >= 0:
        complete[new_index] = max_job
    return iterate_job_sequence(available, complete)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage='Usage: please provide a list of profits and a list of deadlines')
    parser.add_argument('profits', type=input_list)
    parser.add_argument('deadlines', type=input_list)
    args = parser.parse_args()

    jobs = [Job(p, d) for p, d in zip(args.profits, args.deadlines)]

    print(max_profit(jobs))
