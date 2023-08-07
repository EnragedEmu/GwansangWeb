import streamlit as st
import numpy as np

# MBTI 예측 함수 (이 부분은 실제 예측 로직에 따라 구현해야 합니다.)
def predict_mbti(image):
    # 여기에 실제 모델 호출 코드를 추가해야 합니다.
    return "ENFP", {"E": 70, "I": 30, "N": 60, "S": 40, "T": 30, "F": 70, "P": 70, "J": 30}

def display_custom_progress_bar(title_left, title_right, value):
    """사용자 정의 프로그레스 바 표시 함수."""
    # HTML 템플릿
    template = f"""
    <style>
        .progress-wrapper {{
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            margin: 20px 0;  <!-- 프로그레스 바 사이의 간격을 조정 -->
        }}
        .progress-label-left, .progress-label-right {{
            width: 10%;
            text-align: center;  <!-- 글자를 가운데 정렬 -->
        }}
        .progress-container {{
            width: 80%;
            height: 20px;
            background: #f0f0f0;
            border-radius: 5px;
            overflow: hidden;
        }}
        .progress-bar {{
            height: 100%;
            background: #4caf50;
            width: {value}%;
        }}
    </style>
    <div class="progress-wrapper">
        <div class="progress-label-left">{title_left}</div>
        <div class="progress-container">
            <div class="progress-bar"></div>
        </div>
        <div class="progress-label-right">{title_right}</div>
    </div>
    """
    st.markdown(template, unsafe_allow_html=True)

# MBTI 설명을 반환하는 함수
def get_mbti_description(mbti_type):
    descriptions = {
        "ENFP": "재기발랄한 활동가",
        "INTP": "논리적인 사색가",
        # 추가적인 성격유형 설명을 여기에 추가할 수 있습니다.
    }
    return descriptions.get(mbti_type)

# 메인 함수
def main():
    st.markdown("""
    <style>
        [data-testid="block-container"] {
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)
    st.title("너의 관상은")  # 요소1
    st.markdown("셀카를 올리면 매우 과학적인 AI가 MBTI를 예측해드립니다! 당신의 관상은 어떤 MBTI일까요?")  # 요소2

    uploaded_image = st.empty()  # 요소3 (빈 사진 박스)
    image_file = st.file_uploader("사진 업로드", type=["jpg", "png"])  # 요소4

    if image_file:
        uploaded_image.image(image_file, use_column_width=True)
        mbti, scores = predict_mbti(image_file)

        st.markdown("**당신의 관상은...**", unsafe_allow_html=True)

        box_content = f"""
        <div style="border:2px solid gray; padding:20px; border-radius:10px;">
            <div style="font-size:48px; font-weight:bold;">{mbti}</div>
            <div style="font-size:24px;"><i>{get_mbti_description(mbti)}</i></div>
        </div>
        """
        st.markdown(box_content, unsafe_allow_html=True)  # 요소5

        for key, value in scores.items():
            if key in ["E", "N", "T", "P"]:
                opposite_key = "I" if key == "E" else "S" if key == "N" else "F" if key == "T" else "J"
                if scores[key] >= 50:
                    display_custom_progress_bar(key, opposite_key, scores[key])
                else:
                    display_custom_progress_bar(opposite_key, key, 100 - scores[key])


if __name__ == '__main__':
    main()
