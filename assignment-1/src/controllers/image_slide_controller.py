import os
from models.image_slide import ImageSlide
from models.image_node import ImageNode


class ImageSlideController:
    """
    이미지 슬라이드 쇼를 관리하는 컨트롤러
    """

    def __init__(self):
        self.__image_slide = ImageSlide()

    def add_folder(self, folder_path: str):
        """
        이미지 폴더에서 이미지를 불러와서 슬라이드 쇼에 추가하는 함수
        """

        # 폴더가 아닐 경우
        if not os.path.isdir(folder_path):
            print("폴더가 아닙니다.")
            return

        # 폴더 내의 파일 목록을 가져온 다음, 파일의 생성 날짜를 기준으로 정렬
        image_files = [filename for filename in os.listdir(
            folder_path) if filename.endswith(('.png', '.jpg', '.jpeg'))]

        # 이미지가 없을 경우
        if not image_files:
            print("이미지가 없습니다.")
            return

        image_files.sort(key=lambda x: os.path.getctime(
            os.path.join(folder_path, x)))

        new_image_slide = ImageSlide()

        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            image_createdAt = os.path.getctime(image_path).as_integer_ratio()

            new_image_node = ImageNode(image_file, image_path, image_createdAt)
            new_image_slide.append(new_image_node)

        self.__image_slide.merge(new_image_slide)

    def add_image(self, image_name: str, image_path: str, created_at: int):
        """
        새로운 이미지를 슬라이드 쇼에 추가하는 함수
        """
        new_image_node = ImageNode(image_name, image_path, created_at)
        print(f"add image: {image_name}, set current image")
        self.__image_slide.append(new_image_node)

    def get_current_image(self) -> str:
        """
        현재 슬라이드 쇼에서 보여지고 있는 이미지를 반환하는 함수
        """
        self.__image_slide.display()
        return self.__image_slide.get_current()

    def next_image(self) -> str:
        """
        다음 이미지를 반환하는 함수
        """
        return self.__image_slide.next_image()

    def prev_image(self) -> str:
        """
        이전 이미지를 반환하는 함수
        """
        return self.__image_slide.prev_image()

    def delete_current(self):
        self.__image_slide.delete_current()
