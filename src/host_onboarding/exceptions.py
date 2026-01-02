"""
Custom Exceptions for Host Onboarding
======================================
"""


class OnboardingError(Exception):
    """Base exception for onboarding errors"""
    
    def __init__(self, message: str, error_code: str = None, details: dict = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.details = details or {}


class ListingNotFoundError(OnboardingError):
    """No listings found at the specified address"""
    
    def __init__(self, address: str):
        super().__init__(
            message=f"Aucune annonce Airbnb trouvée à cette adresse: {address}",
            error_code="LISTING_NOT_FOUND",
            details={"address": address},
        )
        self.address = address


class VerificationFailedError(OnboardingError):
    """Verification attempt failed"""
    
    def __init__(self, message: str, method: str, can_retry: bool = True):
        super().__init__(
            message=message,
            error_code="VERIFICATION_FAILED",
            details={"method": method, "can_retry": can_retry},
        )
        self.method = method
        self.can_retry = can_retry


class SessionExpiredError(OnboardingError):
    """Onboarding session has expired"""
    
    def __init__(self, session_id: str):
        super().__init__(
            message="La session d'onboarding a expiré. Veuillez recommencer.",
            error_code="SESSION_EXPIRED",
            details={"session_id": session_id},
        )
        self.session_id = session_id


class MaxAttemptsReachedError(OnboardingError):
    """Maximum verification attempts reached"""
    
    def __init__(self, max_attempts: int):
        super().__init__(
            message=f"Nombre maximum de tentatives atteint ({max_attempts}). Contactez le support.",
            error_code="MAX_ATTEMPTS_REACHED",
            details={"max_attempts": max_attempts},
        )
        self.max_attempts = max_attempts


class ListingAlreadyConnectedError(OnboardingError):
    """Listing is already connected to an account"""
    
    def __init__(self, listing_id: str, user_id: str = None):
        super().__init__(
            message="Cette annonce est déjà connectée à un compte.",
            error_code="LISTING_ALREADY_CONNECTED",
            details={"listing_id": listing_id},
        )
        self.listing_id = listing_id


class InvalidSessionStateError(OnboardingError):
    """Session is in invalid state for the requested operation"""
    
    def __init__(self, current_status: str, expected_status: str):
        super().__init__(
            message=f"État de session invalide: {current_status}. Attendu: {expected_status}",
            error_code="INVALID_SESSION_STATE",
            details={"current": current_status, "expected": expected_status},
        )
