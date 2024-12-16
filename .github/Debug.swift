import Foundation

enum ServiceEnvironment: Int {
    case dev = 0
    case qaa
    case preprod
    case prod

    var serviceUrl: String {
        switch self {
        case .dev:
            return {var}
        case .qaa:
            return {var}
        case .preprod:
            return {var}
        case .prod:
            return {var}
        }
    }
    
    var baseDomain: String {
        switch self {
        case .dev:
            return "https://dev"
        case .qaa:
            return "https://qa"
        case .preprod:
            return "https://preprod"
        case .prod:
            return "https://prod"
        }
    }

    var name: String {
        switch self {
        case .dev:
            return "DEV"
        case .qaa:
            return "QA"
        case .preprod:
            return "PRE"
        case .prod:
            return "PROD"
        }
    }
}

public struct DebugDrawerModel: Identifiable {
    public var id: UUID
    public var request: String
    public var requestBody: String
    public var responseBody: String
}
