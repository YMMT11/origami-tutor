import pyttsx3
import time
#from check_origamis import check_origami


# =========================================================
# 音声
# =========================================================

engine = pyttsx3.init()

def speak(text):
    try:
        engine.stop()
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        pass

# =========================================================
# 折り紙チューター：ハートの折り方
# 手順管理プログラム
# =========================================================

STEPS = [
    {
        "step": 1,
        "instruction": "Fold the top corner down to the center crease.",
        "image": "images/STEP1.png"
    },# 上の角を中心線に合うように折る

    {
        "step": 2,
        "instruction": "Fold the bottom corner up to the crease on the top edge.",
        "image": "images/STEP2.png"
    },# 下の角が上の辺の中心に合うように折る

    {
        "step": 3,
        "instruction": "Fold the lower left and lower right edges diagonally toward the center crease.",
        "image": "images/STEP3.png"
    },# 下の辺を中央線に向かって左右に折る

    {
        "step": 4,
        "instruction": "Fold the top and the four side corners backward as shown in the picture.",
        "image": "images/STEP4.png"
    },# 裏返し、4つの角を折ると完成する

    {
        "step": 5,
        "instruction": "fin.",
        "image": "images/STEP5.png"
    }
]


# ---------------------------------------------------------
#  手順管理クラス
# ---------------------------------------------------------

class OrigamiTutor:

    def __init__(self, steps):
        self.steps = steps
        self.current_step = 0
        self.finished = False

    # ---------------------------------------------
    # 現在の手順を取得
    # ---------------------------------------------
    def get_current_step(self):

        if self.finished:
            return None

        return self.steps[self.current_step]

    # --------------------------------------------- 
    # CVに渡す現在のステップ番号を取得 
    # --------------------------------------------- 
    def get_current_step_number(self):

        if self.finished: 
            return None 

        return self.steps[self.current_step]["step"]

    # ---------------------------------------------
    # 現在の指示を表示
    # ---------------------------------------------
    def show_instruction(self):

        step = self.get_current_step()

        if step is None:
            print("\n===============================")
            print("Your origami heart is complete!")
            print("===============================")

            speak("Finished!")

            return

        print("\n----------------------")
        print(f"Step {step['step']}")
        print(step["instruction"])
        print("----------------------")

        speak(step["instruction"])

    # ---------------------------------------------
    # CV判定を受け取る
    # ---------------------------------------------
    def receive_cv_result(self, result):

        # True = 正しく折れた
        if result:

            print("Correct!")
            self.next_step()

        # False = まだ正しくない
        else:

            print("Not correct yet.")
            print("Please continue the same step.")

    # ---------------------------------------------
    # 次の手順へ
    # ---------------------------------------------
    def next_step(self):

        self.current_step += 1

        if self.current_step >= len(self.steps):

            self.finished = True

            print("\n======================================")
            print("     Your origami heart is complete!")
            print("======================================")

        else:

            print("\nMoving to the next step.")
            speak("Moving to the next step.")
            

    # ---------------------------------------------
    # 完成したか
    # ---------------------------------------------
    def is_finished(self):

        return self.finished


# =========================================================
# CV担当との接続
# =========================================================

#def wait_for_cv_result(step):

    # 現在のステップ番号を私、True / Falseの判定結果を受け取る
    
#    return check_origami(step)

# ---------------------------------------------------------
#  メイン処理
# ---------------------------------------------------------

#def main():

#    tutor = OrigamiTutor(STEPS)

#    print("==============================")
#    print("  How to Fold an Origami")
#    print("          Heart")
#    print("==============================")

    # 最初の指示を一度だけ表示・音声案内
#    tutor.show_instruction()

#    while not tutor.is_finished():

        # 現在のステップ番号を取得
#        current_step = tutor.get_current_step_number()

        # CV担当から判定を受け取る
#        cv_result = wait_for_cv_result(current_step)

        # CV結果を手順管理に渡す
#        tutor.receive_cv_result(cv_result)

        # 正しく折れた場合、次のステップを音声案内
#        if cv_result and not tutor.is_finished():
#            tutor.show_instruction()

#        time.sleep(1)


# ---------------------------------------------------------
#  実行
# ---------------------------------------------------------

#if __name__ == "__main__":
#    main()
