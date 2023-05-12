# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
)

from google.cloud.support_v2.types import case, case_service


class ListCasesPager:
    """A pager for iterating through ``list_cases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.support_v2.types.ListCasesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``cases`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCases`` requests and continue to iterate
    through the ``cases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.support_v2.types.ListCasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., case_service.ListCasesResponse],
        request: case_service.ListCasesRequest,
        response: case_service.ListCasesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.support_v2.types.ListCasesRequest):
                The initial request object.
            response (google.cloud.support_v2.types.ListCasesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = case_service.ListCasesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[case_service.ListCasesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[case.Case]:
        for page in self.pages:
            yield from page.cases

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCasesAsyncPager:
    """A pager for iterating through ``list_cases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.support_v2.types.ListCasesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``cases`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCases`` requests and continue to iterate
    through the ``cases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.support_v2.types.ListCasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[case_service.ListCasesResponse]],
        request: case_service.ListCasesRequest,
        response: case_service.ListCasesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.support_v2.types.ListCasesRequest):
                The initial request object.
            response (google.cloud.support_v2.types.ListCasesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = case_service.ListCasesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[case_service.ListCasesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[case.Case]:
        async def async_generator():
            async for page in self.pages:
                for response in page.cases:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchCasesPager:
    """A pager for iterating through ``search_cases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.support_v2.types.SearchCasesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``cases`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchCases`` requests and continue to iterate
    through the ``cases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.support_v2.types.SearchCasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., case_service.SearchCasesResponse],
        request: case_service.SearchCasesRequest,
        response: case_service.SearchCasesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.support_v2.types.SearchCasesRequest):
                The initial request object.
            response (google.cloud.support_v2.types.SearchCasesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = case_service.SearchCasesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[case_service.SearchCasesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[case.Case]:
        for page in self.pages:
            yield from page.cases

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchCasesAsyncPager:
    """A pager for iterating through ``search_cases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.support_v2.types.SearchCasesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``cases`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchCases`` requests and continue to iterate
    through the ``cases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.support_v2.types.SearchCasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[case_service.SearchCasesResponse]],
        request: case_service.SearchCasesRequest,
        response: case_service.SearchCasesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.support_v2.types.SearchCasesRequest):
                The initial request object.
            response (google.cloud.support_v2.types.SearchCasesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = case_service.SearchCasesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[case_service.SearchCasesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[case.Case]:
        async def async_generator():
            async for page in self.pages:
                for response in page.cases:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchCaseClassificationsPager:
    """A pager for iterating through ``search_case_classifications`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.support_v2.types.SearchCaseClassificationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``case_classifications`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchCaseClassifications`` requests and continue to iterate
    through the ``case_classifications`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.support_v2.types.SearchCaseClassificationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., case_service.SearchCaseClassificationsResponse],
        request: case_service.SearchCaseClassificationsRequest,
        response: case_service.SearchCaseClassificationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.support_v2.types.SearchCaseClassificationsRequest):
                The initial request object.
            response (google.cloud.support_v2.types.SearchCaseClassificationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = case_service.SearchCaseClassificationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[case_service.SearchCaseClassificationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[case.CaseClassification]:
        for page in self.pages:
            yield from page.case_classifications

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchCaseClassificationsAsyncPager:
    """A pager for iterating through ``search_case_classifications`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.support_v2.types.SearchCaseClassificationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``case_classifications`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchCaseClassifications`` requests and continue to iterate
    through the ``case_classifications`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.support_v2.types.SearchCaseClassificationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[case_service.SearchCaseClassificationsResponse]
        ],
        request: case_service.SearchCaseClassificationsRequest,
        response: case_service.SearchCaseClassificationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.support_v2.types.SearchCaseClassificationsRequest):
                The initial request object.
            response (google.cloud.support_v2.types.SearchCaseClassificationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = case_service.SearchCaseClassificationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[case_service.SearchCaseClassificationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[case.CaseClassification]:
        async def async_generator():
            async for page in self.pages:
                for response in page.case_classifications:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
