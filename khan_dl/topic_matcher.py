from fuzzywuzzy import process
from fuzzywuzzy import fuzz


class Topic_Matcher:
    def __init__(self, scraped_video_topics, yt_video_id_topics):
        self.scraped_video_topics = scraped_video_topics
        self.yt_video_id_topics = yt_video_id_topics

    def first_pass(self):
        """ Returns a dict of Video Topics and IDs that match the most with the
        scraped topics """
        ratio_list = []
        final_dict = {}
        for topic in self.scraped_video_topics:
            for video_topic, video_id in self.yt_video_id_topics.items():
                simple_ratio = fuzz.ratio(
                    topic.lower().strip(), video_topic.lower().strip(),
                )
                ratio_list.append(simple_ratio)

            print(max(ratio_list))
            final_dict[topic] = list(self.yt_video_id_topics.values())[
                ratio_list.index(max(ratio_list))
            ]
            ratio_list.clear()
        return final_dict

    def second_pass(self):
        pass
