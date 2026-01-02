"""
Host Onboarding Service
========================

Professional onboarding flow for Airbnb hosts:
1. Search by address → Find listings
2. Select listing → Host chooses their property
3. Verify ownership → Prove it's really theirs
4. Complete → Access granted

100% Legal - No Airbnb credentials required!
"""

__version__ = "1.0.0"
__author__ = "Rbie - HostTools Project"

# Main service
from .service import OnboardingService

# Verification
from .verification import (
    VerificationMethod,
    VerificationRequest,
    VerificationResult,
    VerificationStatus,
    TitleCodeVerifier,
    ScreenshotVerifier,
    ICalVerifier,
    VerificationManager,
)

# Models
from .models import (
    OnboardingSession,
    OnboardingStatus,
    HostProfile,
    ConnectedListing,
    ListingMatch,
    VerificationCode,
    utc_now,
)

# Exceptions
from .exceptions import (
    OnboardingError,
    ListingNotFoundError,
    VerificationFailedError,
    SessionExpiredError,
    MaxAttemptsReachedError,
    ListingAlreadyConnectedError,
    InvalidSessionStateError,
)

__all__ = [
    "__version__",
    "OnboardingService",
    "VerificationMethod",
    "VerificationRequest",
    "VerificationResult",
    "VerificationStatus",
    "TitleCodeVerifier",
    "ScreenshotVerifier",
    "ICalVerifier",
    "VerificationManager",
    "OnboardingSession",
    "OnboardingStatus",
    "HostProfile",
    "ConnectedListing",
    "ListingMatch",
    "VerificationCode",
    "utc_now",
    "OnboardingError",
    "ListingNotFoundError",
    "VerificationFailedError",
    "SessionExpiredError",
    "MaxAttemptsReachedError",
    "ListingAlreadyConnectedError",
    "InvalidSessionStateError",
]
