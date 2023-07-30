from ..utils.request_gen import APICaller
from ..utils.routes import USER_INFO
from ..utils import DATA
import pytest


class TestUserInfo:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_fetch_user_info(self, get_api_obj: APICaller):
        """
        This test is to fetch user info
        """
        url_offset = USER_INFO.GET_USER_INFO
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)
        for contact in contacts:
            assert "emails" in contact
            assert "phone_numbers" in contact

    @pytest.mark.regression
    def test_fetch_user_info_by_phone_number(self, get_api_obj: APICaller):
        """
        This test is to fetch user info by phone_number
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?phone_number={DATA.PHONE_NUMBER}"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)
        for contact in contacts:
            phone_numbers = [contact["value"] for contact in contact["phone_numbers"]]
            assert DATA.PHONE_NUMBER in phone_numbers

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_fetch_user_info_by_email(self, get_api_obj: APICaller):
        """
        This test is to fetch the user info by email
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?email={DATA.EMAIL}"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)
        for contact in contacts:
            emails = [contact["value"] for contact in contact["emails"]]
            assert DATA.EMAIL in emails

    @pytest.mark.regression
    def test_fetch_user_info_desc(self, get_api_obj: APICaller):
        """
        This test is to verify the lists API with oder=desc is a list
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order=desc"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)

    @pytest.mark.regression
    def test_fetch_user_info_asc(self, get_api_obj: APICaller):
        """
        This test is to verify the lists API with oder=asc is a list
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order=asc"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_fetch_user_info_created_at(self, get_api_obj: APICaller):
        """
        This test is to fetch the user list when we give orderby with created at information
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order_by=created_at"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)

    @pytest.mark.regression
    def test_fetch_user_info_updated_at(self, get_api_obj: APICaller):
        """
        This test is to fetch the user list when we give orderby with updated at information
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order_by=updated_at"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_fetch_user_info_all_parms(self, get_api_obj: APICaller):
        """
        This is the testcase when we provide the given number
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order=asc&order_by=created_at&phone_number={DATA.PHONE_NUMBER}"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)
        for contact in contacts:
            phone_numbers = [contact["value"] for contact in contact["phone_numbers"]]
            email_id = [contact["value"] for contact in contact["emails"]]
            assert DATA.PHONE_NUMBER in phone_numbers and DATA.EMAIL in email_id

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_fetch_user_info_with_wrong_phone_number(self, get_api_obj: APICaller):
        """
        This is a negative testcase when we provide a number which is wrong
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order=asc&order_by=created_at&phone_number={DATA.WRONG_NUMBER}"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert (
            isinstance(contacts, list) and len(contacts) == 0
        ), "The 'contacts' list should be empty."

    @pytest.mark.regression
    def test_fetch_user_info_with_0_phone_number(self, get_api_obj: APICaller):
        """
        This is a negative testcase when we provide phone number as 0
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order=asc&order_by=created_at&phone_number={DATA.ZERO_NUMBER}"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list) and len(contacts) == 0, "The 'contacts' list should be empty."

    @pytest.mark.regression
    def test_fetch_user_info_with_negative_phone_number(self, get_api_obj: APICaller):
        """
        This is a negative testcase when we provide a number which is -ve
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order=asc&order_by=created_at&phone_number={DATA.NEGATIVE_NUMBER}"
        data = get_api_obj.get(url_offset, skip_err=True)
        status_value = data["errors"][0]["status"]
        assert status_value == 400

    @pytest.mark.regression
    def test_fetch_user_info_with_aphanumeric_phone_number(
        self, get_api_obj: APICaller
    ):
        """
        This is a negative testcase when we provide a number which is alphanumeric
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order=asc&order_by=created_at&phone_number={DATA.ALPHANUMBERIC_NUMBER}"
        data = get_api_obj.get(url_offset, skip_err=True)
        status_value = data["errors"][0]["status"]
        assert status_value == 400
