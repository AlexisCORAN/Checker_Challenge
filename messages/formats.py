#!/usr/bin/python3
import discord
import storage

def tasks_fmt(tasks):
    tasks_str = '\n'.join(list(
            map(
                lambda i, t: '\t`Task {}:` {}'.format(i, t.get('title', '')),
                range(len(tasks)), tasks)
            ))
    return '**Tasks ({}):**\n{}'.format(len(tasks), tasks_str)

def checks_fmt(checks, all_passed=False, commit_id=None):
    number_passed_checks = 0
    for i in checks:
        if i.get('passed', '') == True:
            number_passed_checks += 1
    number_no_passed_checks = len(checks) - number_passed_checks
    print(number_passed_checks)
    print(number_no_passed_checks)

    checks_str = '  '.join(list(
            map(
                lambda t: '\t`{} {}`'.format('✅' if t.get('passed', '') else '❌', t.get('title', '')),
                checks)
            ))
    score = round((number_passed_checks/len(checks))*100, 2)
    message = "*Some checks are failing.* Make sure you fix them before starting a new review\nYou got this!"
    if all_passed is True:
        message = "*Congratulations!* All tests passed successfully!\nYou are ready for your next mission!"
    check_title = storage.task.get('title')
    return '**Correction of \"{}\"** \nCommit ID used: {}\n\n{}\n\n**Score: {} %**\n**Result:**\n{}'.format(check_title, commit_id, message, score, checks_str)

def embeded_project_fmt(title='', _id='', desc='', error=True, url=None):
    if url is None:
        url="https://intranet.hbtn.io/projects/{}".format(_id)
        
    return discord.Embed(title=title,
            color=13632027 if error is True else 4886754,
            url=url,
            icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg",
            description=desc,
            thumbnail="https://cdn.discordapp.com/embed/avatars/0.png",
        )
