# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import music_pb2 as music__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in music_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class MusicServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSong = channel.unary_unary(
                '/MusicService/GetSong',
                request_serializer=music__pb2.SongRequest.SerializeToString,
                response_deserializer=music__pb2.SongResponse.FromString,
                _registered_method=True)
        self.GetFeaturedAlbums = channel.unary_unary(
                '/MusicService/GetFeaturedAlbums',
                request_serializer=music__pb2.Empty.SerializeToString,
                response_deserializer=music__pb2.AlbumList.FromString,
                _registered_method=True)


class MusicServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSong(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFeaturedAlbums(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MusicServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSong': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSong,
                    request_deserializer=music__pb2.SongRequest.FromString,
                    response_serializer=music__pb2.SongResponse.SerializeToString,
            ),
            'GetFeaturedAlbums': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFeaturedAlbums,
                    request_deserializer=music__pb2.Empty.FromString,
                    response_serializer=music__pb2.AlbumList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MusicService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('MusicService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MusicService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/MusicService/GetSong',
            music__pb2.SongRequest.SerializeToString,
            music__pb2.SongResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetFeaturedAlbums(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/MusicService/GetFeaturedAlbums',
            music__pb2.Empty.SerializeToString,
            music__pb2.AlbumList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)