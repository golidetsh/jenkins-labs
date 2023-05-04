FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src/Facebook
COPY ["Facebook.csproj", "./"]
RUN dotnet restore "./Facebook.csproj"
COPY . .
RUN dotnet build "Facebook.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Facebook.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Facebook.dll"]