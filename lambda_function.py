# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

from refer_to_opendata import refer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 北海道オープンデータポータルのデータを参照
obj = refer('https://www.harp.lg.jp/opendata/dataset/1369/resource/2853/covid19_data.csv', 'shift-jis')

# obj[0] -> year, # 年
# obj[1] -> month, # 月
# obj[2] -> day, # 日
# obj[3] -> inspections_per_day, # 日検査数
# obj[4] -> inspections_total, # 検査累計
# obj[5] -> positives_per_day, # 日陽性数
# obj[6] -> positives_total, # 陽性累計
# obj[7] -> patients_per_day, # 日患者数
# obj[8] -> patients_totals, # 患者累計
# obj[9] -> mild_per_day, # 日軽症中等症数
# obj[10] -> mild_total, # 軽症中等症累計
# obj[11] -> serious_injury_per_day, # 日重症数
# obj[12] -> serious_injury_total, # 重症累計
# obj[13] -> deaths_per_day, # 日死亡数
# obj[14] -> deaths_total, # 死亡累計
# obj[15] -> finished_treatment_per_day, # 日治療終了数
# obj[16] -> finished_treatment_total) # 治療終了累計

# 発話や画面表示内容
# 発話の間の調整
break_200ms = '<break time=\"200ms\"/>'
break_300ms = '<break time=\"300ms\"/>'
break_400ms = '<break time=\"400ms\"/>'
break_700ms = '<break time=\"700ms\"/>'

SPEECH_TEXT = f'{break_300ms}{obj[0]}年{obj[1]}月{obj[2]}日の情報です。' \
              f'{break_300ms}新たな陽性患者は{obj[5]}人' \
              f'{break_300ms}これまでの累計は{obj[6]}人になりました。' \
              f'{break_300ms}現在の患者は{obj[8]}人です。' \
              f'{break_300ms}一方、新たに治療が終了したかたは{obj[15]}人' \
              f'{break_300ms}これまでの累計は{obj[16]}人になりました。' \
              f'{break_300ms}検査したかたはあらたに{obj[3]}人' \
              f'{break_300ms}これまでの累計は{obj[4]}人です。'

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
#        speak_output = "Welcome, you can say Hello or Help. Which would you like to try?"
        speak_output = SPEECH_TEXT

        return (
            handler_input.response_builder
                .speak(speak_output)
#                .ask(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "北海道オープンデータポータルの、新型コロナウイルス感染症に関するデータ北海道のデータから、最新の新型コロナウイルス情報をお知らせします。"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "わかりました"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "すみません。わかりませんでした。もう一度言ってください。"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
