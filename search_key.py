import vk_api

from config import API_TOKEN, token


session = vk_api.VkApi(token=token)



def last_two():
    '''
    при команде старт отправляет 2 последних объявления в чат
    :return:
    '''
    domain = 'arenda_v_moskv'
    count = 2
    offset = 0
    wall = session.method('wall.get', {'domain': domain,
                                       'count': count,
                                       'offset': offset})
    all_post = []
    all_post.append(wall)
    for post in all_post[0]['items']:
        print(post['attachments'][-1]['link']['url'])

last_two()